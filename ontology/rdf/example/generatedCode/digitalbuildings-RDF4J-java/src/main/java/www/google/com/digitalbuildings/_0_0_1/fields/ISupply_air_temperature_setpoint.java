package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ITemperature;
import www.google.com.digitalbuildings._0_0_1.subfields.ISupply;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;

public interface ISupply_air_temperature_setpoint extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfSetpoint (ISetpoint parameter);

	public Set<ISetpoint> getComposedOfSetpoint();

    public void addComposedOfSupply (ISupply parameter);

	public Set<ISupply> getComposedOfSupply();

    public void addComposedOfTemperature (ITemperature parameter);

	public Set<ITemperature> getComposedOfTemperature();

}