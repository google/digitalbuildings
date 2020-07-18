package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICondenser;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressure;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ICondenser_pressure_sensor extends IField{

	public IRI iri();

    public void addComposedOfCondenser (ICondenser parameter);

	public Set<ICondenser> getComposedOfCondenser();

    public void addComposedOfPressure (IPressure parameter);

	public Set<IPressure> getComposedOfPressure();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}