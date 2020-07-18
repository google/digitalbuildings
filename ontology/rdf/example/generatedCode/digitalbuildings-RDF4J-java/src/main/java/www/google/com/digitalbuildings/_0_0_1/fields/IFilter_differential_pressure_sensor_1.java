package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IDifferential;
import www.google.com.digitalbuildings._0_0_1.subfields.IFilter;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressure;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IFilter_differential_pressure_sensor_1 extends IField{

	public IRI iri();

    public void addComposedOfDifferential (IDifferential parameter);

	public Set<IDifferential> getComposedOfDifferential();

    public void addComposedOfFilter (IFilter parameter);

	public Set<IFilter> getComposedOfFilter();

    public void addComposedOfPressure (IPressure parameter);

	public Set<IPressure> getComposedOfPressure();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}