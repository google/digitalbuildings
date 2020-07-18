package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.IDifferential;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IProcess;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressure;

public interface IProcess_water_differential_pressure_setpoint extends IField{

	public IRI iri();

    public void addComposedOfDifferential (IDifferential parameter);

	public Set<IDifferential> getComposedOfDifferential();

    public void addComposedOfPressure (IPressure parameter);

	public Set<IPressure> getComposedOfPressure();

    public void addComposedOfProcess (IProcess parameter);

	public Set<IProcess> getComposedOfProcess();

    public void addComposedOfSetpoint (ISetpoint parameter);

	public Set<ISetpoint> getComposedOfSetpoint();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}