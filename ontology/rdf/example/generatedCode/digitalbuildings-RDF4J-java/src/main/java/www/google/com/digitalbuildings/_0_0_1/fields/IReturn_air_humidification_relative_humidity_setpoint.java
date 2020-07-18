package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IRelative;
import www.google.com.digitalbuildings._0_0_1.subfields.IReturn;
import www.google.com.digitalbuildings._0_0_1.subfields.IHumidity;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IHumidification;

public interface IReturn_air_humidification_relative_humidity_setpoint extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfHumidification (IHumidification parameter);

	public Set<IHumidification> getComposedOfHumidification();

    public void addComposedOfHumidity (IHumidity parameter);

	public Set<IHumidity> getComposedOfHumidity();

    public void addComposedOfRelative (IRelative parameter);

	public Set<IRelative> getComposedOfRelative();

    public void addComposedOfReturn (IReturn parameter);

	public Set<IReturn> getComposedOfReturn();

    public void addComposedOfSetpoint (ISetpoint parameter);

	public Set<ISetpoint> getComposedOfSetpoint();

}